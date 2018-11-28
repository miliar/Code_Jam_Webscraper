#include <bits/stdc++.h>

using namespace std;

#define MAX 2147483647
#define MIN -2147483647
#define clear_arr(a) memset(a,0,sizeof(a))
#define pb push_back
#define pi 3.14159265358979323846

typedef int ll;
typedef pair<ll,ll> ii;
typedef pair<string,string> ss;
typedef vector<ss> vss;
typedef pair<ll, ii> iii;
typedef pair<double,double>  dd;
typedef vector<ll> vi;
typedef vector<ii> vii;
typedef vector<iii> viii;
typedef vector<string> vs;
typedef vector<ii> vii;
typedef deque<ll> dqi;
typedef unordered_set<ll> usi;
typedef set<ll> si;
typedef unordered_set<ii> usii;
typedef set<ii> sii;
typedef unordered_map<ll,ll> umii;
typedef map<ll,ll> mii; 
typedef map<string,int> msi;
typedef map<int,string> mis;

ii cam[1003], jam[1003];
int ac, aj;


bool my_comp(ii a, ii b){
	return a.first < b.first ;
}

int main(){
	int cases;
	scanf("%d",&cases);
	int changes;
	int temp;
	for(int xl=1;xl<=cases;xl++){
		scanf("%d %d", &ac, &aj);
		for(int i=0;i<ac;i++)
			scanf("%d %d", &cam[i].first, &cam[i].second);
		for(int i=0;i<aj;i++)
			scanf("%d %d", &jam[i].first, &jam[i].second);
		sort(cam, cam+ac, my_comp);
		sort(jam, jam+aj, my_comp);
		printf("Case #%d: ", xl);
		changes = 0;
		if(aj + ac == 1){
			printf("2\n");
		}
		else if(aj == 0){
			if(1440 - cam[1].second + cam[0].first >= 720 or cam[1].first - cam[0].second >= 720)
				printf("2\n");
			else
				printf("4\n");
		}else if(ac == 0){
			if(1440 - jam[1].second + jam[0].first >= 720 or jam[1].first - jam[0].second >= 720)
					printf("2\n");
			else
				printf("4\n");

		}else{
			printf("2\n");
		}
	}
	return 0;
}