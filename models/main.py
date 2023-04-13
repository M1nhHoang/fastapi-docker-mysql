from fastapi import FastAPI, Request
from sqlDataAccess import sqlDataAccess

app = FastAPI()
sql = sqlDataAccess()

# create middleware
@app.on_event("startup")
async def startup():
	# connect to database
    await sql.connect()

# create api end-point
@app.post("/insert")
async def input(request: Request):
	try:
		# if not error
		# get payload
		payload = await request.json()
		names = [item['name'] for item in payload]
		phones = [item['phone'] for item in payload]
		# excute
		await sql.execute_storedProcedure('psAddPerson', [names, phones])
		return {"status": 200,
				"content": "success"}
	except Exception as e:
		return {"status": 500,
				"content": str(e)}

@app.get("/persons")
async def persons():
	try:
		# if not error
		result = await sql.execute_storedProcedure('psGetPersons')
		return {"status": 200,
				"persons": result}
	except Exception as e:
		return {"status": 500,
				"content": str(e)}

@app.get("/findpersons")
async def findpersons(name: str):
	try:
		# if not error
		result = await sql.execute_storedProcedure('psGetDataWithName', [name])
		return {"status": 200,
				"persons": result}
	except Exception as e:
		return {"status": 500,
				"content": str(e)}


