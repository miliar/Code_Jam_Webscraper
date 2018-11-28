#include<cstdio>
#include<cstdlib>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
#include<iostream>
#include<cmath>

using namespace std;

#define pb push_back
#define mp make_pair

int T,n,k;
pair<long long,long long> p[1005];

const long double pi = 3.1415926535897932;

bool comp(pair<long long,long long> &f, pair<long long,long long> &s){
    return (long long)f.first*f.second > (long long)s.first*s.second;
}

void read_input(){
    cin >> T ;
    cout.precision(17);
    for(int t = 0 ;  t < T ; ++t){
	cin >> n >> k ;
	for(int i = 0 ; i < n; ++i)
	    cin >> p[i].second >> p[i].first ; 

	sort(p,p+n,&comp);

	long double res = 0;
	for(int i = 0; i < n; ++i){
	    long double cur = pi*p[i].second*p[i].second;
	    long long h = p[i].first*p[i].second;

	    int cnt = 1; 
	    for(int j = 0 ; j < n; ++j){
		if(cnt == k )
		    break;
		if(j!=i && p[j].second <= p[i].second){
		    h += p[j].first*p[j].second;
		    ++cnt;
		}
	    }

	    if(cnt == k)
		res = max(res,cur+h*2*pi);
	}

	cout << "Case #" << t+1 << ": " << res << endl;
    }
}

int main(){
    read_input();
    return 0;
}
