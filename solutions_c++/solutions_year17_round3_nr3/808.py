#include <bits/stdc++.h>

using namespace std;

#define MAX 2147483647
#define MIN -2147483647
#define clear_arr(a) memset(a,0,sizeof(a))
#define pb push_back

typedef long long int ll;
typedef pair<ll,ll> ii;
typedef pair<double,double>  dd;
typedef pair<string,string> ss;
typedef vector<ss> vss;
typedef pair<ll, ii> iii;
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

double p[52];
int n,k;
double u;

int count_less_1(){
	int less_1 = 0;
	for(int i=0;i<n;i++){
		if(p[i] < 1.000)
				less_1++;
	}
	return less_1;
}

int main(){
	int cases;
	scanf("%d", &cases);
	double min_diff;
	int counter;
	double prob;
	int index;
	for(int xl=1;xl<=cases;xl++){
		scanf("%d %d", &n, &k);
		scanf("%lf", &u);
		int less_1 = 0;
		for(int i=0;i<n;i++){
			scanf("%lf", &p[i]);
			if(p[i] < 1.000)
				less_1++;
		}
		sort(p, p+n);
		counter = 0;
		double current_min = p[0];
		double diff;
		// printf("%d    %lf   %lf %lf\n",index, diff, p[0], p[1] );
		while(u > 0.0){
			for(index=0;index<n;index++)
				if(p[index] != current_min)
					break;
			if(index < n)
				diff = p[index] - current_min;
			else 
				diff = 0;
			// if(index * diff <= u and diff != 0.0){
			// 	u -= (index*diff);
			// 	for(int i=0;i<index;i++)
			// 		p[i] += diff;
			// }else{
			// 	diff = u/index;
			// 	for(int i=0;i<index;i++)
			// 		p[i] += diff;
			// 	break;
			// }
			if(index == n){
				// printf("'here'\n" );
				diff = u/n;
			}else if(index * diff > u or diff == 0.0){
				// printf("h1\n");
				diff = u/index;
			}else{
			}
			u -= (index*diff);
			for(int i=0;i<index;i++)
				p[i] += diff;
			// printf("%d    %lf   %lf %lf\n",index, diff, p[0], p[1] );
			current_min = p[0];
			if(counter > 1000000)
				break;
			counter++;
		}
		// while(u > 0.0){

		// }
		prob = 1.0;
		for(int i=0;i<n;i++)
			prob *= p[i];
		printf("Case #%d: %.7lf\n",xl, prob );
	}
	return 0;
}