from utils.params import DBParam
from utils.prepare_dataset import DB

def test_case_1():
    _params = DBParam()
    _db = DB(_params)
    print(_db.PARAMS.RECORDS_PATH)
    _db.create_records()


if __name__ == "__main__":
    test_case_1()