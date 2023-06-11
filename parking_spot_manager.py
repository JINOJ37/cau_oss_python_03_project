class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __init__(self, name, city, district, ptype, longitude, latitude):
        """ 생성자
        매개변수: name, city, district, ptype, longitude, latitude

        __item 필드의 생성 및 설정
        """
        self.__item = dict()
        self.__item['name'] = name
        self.__item['city'] = city
        self.__item['district'] = district
        self.__item['ptype'] = ptype
        self.__item['longitude'] = longitude
        self.__item['latitude'] = latitude

    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
    def get(self, keyword='name'):
        """ get 메소드
        매개변수: keyword(기본인수 'name')

        __item의 key(keyword)값의 value 값 반환
        """
        return self.__item[keyword]

def str_list_to_class_list(str_list):
    """ str_list_to_class_list 메소드
    매개변수: str_list(문자열 리스트) -> [순번], [자원명], [시도], [시군구], [주차장유형], [경도], [위도] 데이터 문자열

    parking_spot 클래스 객체의 리스트로 변환 후 반환
    """
    parking_spot_list = list() # parking_spot 클래스 객체의 리스트
    data = list() # 쉼표(,)로 구분한 각 데이터 저장 리스트
    for line in str_list:
        for word in line.split(','): # split 함수 이용 문자열 구분
            data.append(word)

        # data[0]([순번]) 제외/ data[5]([경도]), data[6]([위도]) 는 실수형으로 전환
        parking_spot_list.append(parking_spot(data[1], data[2], data[3], data[4], float(data[5]), float(data[6])))
        data.clear()
    
    return parking_spot_list 

def print_spots(spots):
    """ print_spots 메소드
    매개변수: spots(parking_spot 클래스 객체의 리스트)

    spots 리스트에 저장된 모든 객체의 값 출력
    """
    print(f"---print elements({len(spots)})---")
    for i in spots:
        print(i) # __str__ 메소드 사용
        

# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)
    
    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)