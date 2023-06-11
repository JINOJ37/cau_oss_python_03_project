import file_manager
import parking_spot_manager

def start_process(path):

    # parking_spot_manager 모듈 parking_spot 클래스 객체리스트 생성
    parking_spot_list = parking_spot_manager.str_list_to_class_list(file_manager.read_file(path))

    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))

        if select == 1:
            """ 1번 옵션 [print]
            parking_spot_manager 모듈의 print_spots 함수 호출
            """
            parking_spot_manager.print_spots(parking_spot_list)

        elif select == 2:
            """ 2번 옵션 [filter]
            필터를 할 기준의 키의 종류 5개 중 하나를 선택
            필터 수행 후 기존 객체리스트 삭제 및 반환되는 새로운 리스트 저장
            """
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))

            if select == 1:
                """ [1] name
                parking_spot_manager 모듈의 filter_by_name 함수 호출
                """
                keyword = input('type name:')
                parking_spot_list = parking_spot_manager.filter_by_name(parking_spot_list, keyword)
            
            elif select == 2:
                """ [2] city
                parking_spot_manager 모듈의 filter_by_city 함수 호출
                """
                keyword = input('type city:')
                parking_spot_list = parking_spot_manager.filter_by_city(parking_spot_list, keyword)
            
            elif select == 3:
                """ [3] district
                parking_spot_manager 모듈의 filter_by_district 함수 호출
                """
                keyword = input('type district:')
                parking_spot_list = parking_spot_manager.filter_by_district(parking_spot_list, keyword)
           
            elif select == 4:
                """ [4] ptype
                parking_spot_manager 모듈의 filter_by_ptype 함수 호출
                """
                keyword = input('type ptype:')
                parking_spot_list = parking_spot_manager.filter_by_ptype(parking_spot_list, keyword)
            
            elif select == 5:
                """ [5] location
                parking_spot_manager 모듈의 filter_by_location 함수 호출
                """
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))

                # 튜플[keywords]: 순서대로 최소위도[min_lat], 최대위도[max_lat], 최소경도[min_long], 최대경도[max_long]를 저장
                keywords = (min_lat, max_lat, min_lon, max_lon) 
                parking_spot_list = parking_spot_manager.filter_by_location(parking_spot_list, keywords)
            
            else:
                print("invalid input")

        elif select == 3:
            """ 3번 옵션 [sort]
            필터를 할 기준의 키[keyword]를 문자열로 입력
            
            1)keyword가 keywords 목록에 있다면
            parking_spot_manager 모듈의 sort_by_keyword 함수 호출
            2) 없다면
            출력: "invalid input"

            정렬 수행 후 기존 객체리스트 삭제 및 반환되는 새로운 리스트 저장
            """
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                parking_spot_list = parking_spot_manager.sort_by_keyword(parking_spot_list, keyword)
            else: print("invalid input")

        elif select == 4:
            """ 4번 옵션 [exit]
            출력: "Exit"
            반복 종료
            """
            print("Exit")
            break
        
        else:
            print("invalid input")