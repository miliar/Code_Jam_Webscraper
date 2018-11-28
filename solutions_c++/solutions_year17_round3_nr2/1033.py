// =====================================================================================
// 
//       Filename:  B.cpp
//        Created:  2017년 04월 30일 18시 25분 30초
//       Compiler:  g++ -O2 -std=c++14
//         Author:  baactree ,  bsj0206@naver.com
//        Company:  Chonnam National University
// 
// =====================================================================================

#include <bits/stdc++.h>
using namespace std;
pair<int, int> a[100];
pair<int, int> b[100];

int main(){
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
	int TestCase;
	scanf("%d", &TestCase);
	for(int tc=1;tc<=TestCase;tc++){
		int n, m;
		scanf("%d%d", &n, &m);
		for(int i=0;i<n;i++){
			scanf("%d%d", &a[i].first, &a[i].second);
		}
		for(int i=0;i<m;i++){
			scanf("%d%d", &b[i].first, &b[i].second);
		}
		int ans=0;
		if(n==2){
			sort(a, a+n);
			if(a[1].second-a[0].first<=720)
				ans=2;
			else if(a[0].second+1440-a[1].first<=720)
				ans=2;
			else
				ans=4;
		}
		else if(m==2){
			sort(b, b+m);
			if(b[1].second-b[0].first<=720)
				ans=2;
			else if(b[0].second+1440-b[1].first<=720)
				ans=2;
			else
				ans=4;
		}
		else 
			ans=2;
		printf("Case #%d: %d\n", tc, ans);
	}
	return 0;
}

