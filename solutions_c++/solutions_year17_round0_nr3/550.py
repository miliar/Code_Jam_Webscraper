#include<iostream>
#include<cstdio>
#include<vector>
#include<cstdlib>
#include<cmath>
#include<iomanip>
#include<algorithm>
#include<set>
#include<iomanip>
#include<queue>
#include<map>
#include<deque>

using namespace std;

#define VI vector<int>
#define PI pair<int,int>
#define F first
#define S second
#define MP make_pair
#define LL long long
#define PB push_back
#define VB vector<bool>
#define VS vector<string>
#define VVS vector<VS>

pair<LL,LL> splits(LL l){
	LL a = l/2LL;
	LL b = a;
	if(l % 2LL == 0LL)
		b--;
	return MP(a,b);
}

void printMap(map<LL,LL> mymap){
	printf("printing map:\n");
	for(map<LL,LL>::iterator it=mymap.begin();it != mymap.end();it++){
		printf("slots[%lld] = %lld\n", it->F, it->S);
	}
}

int main()
{
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/quals/C_input3.txt", "r", stdin);
	freopen("/Users/Sharat/GoogleDrive/Coding/C++/Contests/GCJ2017/quals/C_output3.txt", "w", stdout);

	int cases;
	scanf("%d", &cases);

	for(int casenum=1;casenum<=cases;casenum++){
		LL N,K;
		cin>>N>>K;

		map<LL,LL> slots;
        slots[N] = 1LL;

        LL cur = 0;
        pair<LL,LL> res;

        while(true){
			map<LL,LL>::iterator it = slots.end();
			it--;
			LL len = (*it).F;
			LL freq = (*it).S;
			res = splits(len);

			//printMap(slots);
			//printf("current slot is (%lld,%lld) and K = %lld\n", len, freq, K);
			if(freq >= K){
				break;
			}
			else{
				slots.erase(it);

				if(slots.find(res.F) == slots.end()){
					slots[res.F] = freq;
				}
				else{
					slots[res.F] += freq;
				}

				if(slots.find(res.S) == slots.end()){
					slots[res.S] = freq;
				}
				else{
					slots[res.S] += freq;
				}

				K -= freq;
			}
        }
		cout<<"Case #"<<casenum<<": "<<res.F<<" "<<res.S<<endl;
	}

	return 0;
}
