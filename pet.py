import pandas as pd
import numpy as np
import random
import string
from icecream import ic

if __name__ == '__main__':

    data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
            'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
            'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
            'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    df = pd.DataFrame(data, index=[labels])


    menu = int(input('2. 버전\n'
                     '3. 라이브러리정보\n'
                     '4. 주어진 값으로 DataFrame 객체를 생성하시오\n'
                     '5. 객체내부 정보를 출력\n'
                     '6. 객체 상위 3열까지 출력\n'
                     '7. animal과 age 컬럼만 출력\n'
                     '8. 객체의 3, 4, 8번 행에 해당하는 animal과 age 값만 출력\n'
                     '9. visit 컬럼에서 3 초과하는 값 출력\n'
                     '10. age 에서 NaN 값 출력\n'
                     '11. age가 3살 미만 고양이값 출력\n'
                     '12. age가 2살이상 4살 미만인 값 출력\n'
                     '13. f 행의 나이를 1.5살로 변경\n'
                     '14. 객체에서 visit 의 합 출력\n'
                     '15. 동물별로 나이의 평균 출력\n'
                     '16. k행을 추가하여 dog , 5.5세, 방문회수 2회, 우선권없음(no) 열을 추가\n'
                     '16. 방금 추가한 열 삭제\n'
                     '17. 객체에 있는 동물의 종류의 수 출력\n'
                     '18. age 는 내림차순, visits 는 오름차순으로 정렬\n'
                     '19. priority 의 yes를 True, no 를 False  로 맵핑 후 출력\n'
                     '20. snake 를 python 으로 값을 변경\n'
                     '21. 각각의 동물 유형과 방문 횟수에 대해, 평균나이를 찾으시오.즉,각 행은 animal 이고, 각 열은 visits 이며, 값은 평균연령 (힌트, 피벗 테이블을 활용해야 함)\n'))


    def quiz_2():
        ic(pd.__version__)

    def quiz_3():
        ic(pd.show_versions())

    def quiz_4():
        ic(df)

    def quiz_5():
        ic(df.describe())

    def quiz_6():
        ic(df.head(3))

    def quiz_7():
        ic(df.loc[:, ['animal', 'age']])

    def quiz_8():
        ic(df.loc[df.index[[3, 4, 8]], ['animal', 'age']])

    def quiz_9():
        ic(df[df['visits'] >= 3])


    def quiz_10():
        ic(df[df['age'].isnull()])

    def quiz_11():
        ic(df[(df['age'] <= 3) & (df['animal'] == 'cat')])

    def quiz_12():
        ic(df[(df['age'] >= 2) & (df['age'] <= 4)])

    def quiz_13():
        df.loc['f', 'age'] = 1.5

    def quiz_14():
        ic(sum(df['visits']))

    def quiz_15():
        ic(df.groupby('animal')['age'].mean())

    def quiz_16():
        df.loc['k'] = ['dog', 5.5, 2, 'no']
        ic(df)
        df.drop(['k'])
        ic(df)

    def quiz_17():
        ic(df['animal'].value_counts())

    def quiz_18():
        df.sort_values(by=['age', 'visits'], ascending=[False, True])
        ic(df)


    def quiz_19():
        df.replace(['yes', 'no'], ['True', 'False'])
        ic(df)

    def quiz_20():
        df.replace(['snake'], ['python'])
        ic(df)

    def quiz_21():
        df1 = pd.pivot_table(df, index='animal', columns='visits', values='age', aggfunc='mean')
        ic(df1)



