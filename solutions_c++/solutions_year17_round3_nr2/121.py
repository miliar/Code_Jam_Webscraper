#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;
#define PI 3.1415926535897932384626433832795028841971

int T;

struct Interval{
	int left;
	int right;
	int tag;
} interval[1003];

int cmp(const Interval& lhs, const Interval& rhs){
	return lhs.left < rhs.left;
}

int main(){
	cin>>T;
	for(int cs = 1; cs<=T; ++cs){
		int AC, AJ;
		cin>>AC>>AJ;
		for(int i = 0; i< AC; ++i){
			cin>>interval[i].left>>interval[i].right;
			interval[i].tag = 0;
		}

		for(int i = AC; i< AC + AJ; ++i){
			cin>>interval[i].left>>interval[i].right;
			interval[i].tag = 1;
		}
		std::sort(interval, interval+AC+ AJ, cmp);

		int res = 0;

		int pre = interval[0].tag;

		int Ctime = 0;
		int goodtime = 0;

		int badtime[2][233];
		int cnt[2];
		cnt[0]=cnt[1]= 0;
		for(int i = 1; i< AC+AJ; ++i){
			if (interval[i].tag != pre){
				++res;
				goodtime += interval[i].left - interval[i-1].right; 
				if (pre == 0){
					Ctime += interval[i-1].right-interval[i-1].left;
				}
			}else{
				badtime[pre][cnt[pre]++]= (interval[i].left - interval[i-1].right);
				if(pre == 0){
					Ctime += interval[i].left - interval[i-1].left;
				}
			}
			pre = interval[i].tag;
		}
		if(interval[0].tag != interval[AC+AJ-1].tag){
			++res;
			goodtime += interval[0].left + 24 * 60 - interval[AC+AJ-1].right;
			if(interval[AC+AJ-1].tag == 0){
				Ctime+= interval[AC+AJ-1].right - interval[AC+AJ-1].left;
			}
		}else{
			pre = interval[AC+AJ-1].tag;
			badtime[pre][cnt[pre]++]= (interval[0].left+24*60 - interval[AC+AJ-1].right);
			if(pre == 0){
				Ctime += interval[0].left +24*60- interval[AC+AJ-1].left;
			}
		}
		
		if(Ctime <= 720 && Ctime+goodtime >=720){
		}else if(Ctime > 720){
			std::sort(badtime[0], badtime[0]+cnt[0]);
			int target = Ctime - 720;
			int i = cnt[0]-1;
			while(target>0){
				res+=2;
				target -=  badtime[0][i];
				--i;
			}
		}else if(Ctime + goodtime <720){
			std::sort(badtime[1], badtime[1]+cnt[1]);
			int target = 720 - Ctime - goodtime;
			int i = cnt[1]-1;
			while(target>0){
				res+=2;
				target -=  badtime[1][i];
				--i;
			}
		}
		printf("Case #%d: %d\n", cs, res);
	}
	return 0;
}
