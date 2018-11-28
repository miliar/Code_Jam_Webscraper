#include <bits/stdc++.h>

using namespace std;

#define MAX 2147483647
#define MIN -2147483647
#define clear_arr(a) memset(a,0,sizeof(a))
#define pb push_back
#define pi 3.14159265358979323846

typedef long long int ll;
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

dd sizes[1004];
double memo[1004][1004][2];
double max_area, max_radius;
dd max_height;
int n,k;

bool my_comp(dd a, dd b){
	return a.first > b.first or (a.first == b.first and a.second > b.second);
}

double recurse(int current, int selected, bool chosen){
	if(selected == 0){
		return 0.0;
	}
	if(current == n)
		return MIN;
	if(memo[current][selected][0] != -1.0)
		return memo[current][selected][0];
	double area;
	double perim = 2*pi * sizes[current].first * sizes[current].second;
	if(chosen){
		area = perim + recurse(current+1, selected-1, chosen);
	}else{
		area = perim + (pi * sizes[current].first * sizes[current].first) + recurse(current+1, selected-1,true);
	}
	area = max(area, recurse(current+1, selected, chosen));
	memo[current][selected][0] = area;
	return memo[current][selected][0];
}

int main(){
	int cases;
	
	scanf("%d",&cases);
	for(int xl=1;xl<=cases;xl++){
		scanf("%d %d",&n, &k);
		for(int i=0;i<n;i++){
			scanf("%lf %lf", &sizes[i].first, &sizes[i].second);
		}
		for(int i=0;i<1004;i++)
			for(int j=0;j<1004;j++)
				memo[i][j][0] = memo[i][j][1] = -1.0;
		sort(sizes, sizes+n, my_comp);
		recurse(0,k,false);
		max_area = MIN;
		for(int i=0;i<1004;i++){
			for(int j=0;j<1004;j++){
				for(int k=0;k<2;k++){
					max_area = max(max_area, memo[i][j][k]);
				}
			}
		}
		printf("Case #%d: %.7lf\n",xl, max_area);
	}
	return 0;
}