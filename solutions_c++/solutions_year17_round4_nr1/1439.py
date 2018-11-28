#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
using namespace std;

typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<vii> vvii;



int T;

int N,P;


int main(){
	cin>>T;
	
	for(int cn=1;cn<=T;cn++){
		cin>>N>>P;
		vi m(P);
		for(int i=0;i<N;i++){
			int a;cin>>a;
			m[a%P]++;
		}
		// for(int i=0;i<P;i++)
		// 	cout<<m[i]<<' ';
		// cout<<'\n';
		int result=m[0];
		while(m[1]>=1 && m[P-1]>=1 && m[1]+m[P-1]>=2){
			result++;m[1]--;m[P-1]--;
		}
		int a=(m[1]>0?1:P-1);
		if(P==4){
			while(m[a]>=2 && m[2]>=1){
				result++;m[a]-=2;m[2]--;
			}
		}
		// for(int i=0;i<P;i++)
		// 	cout<<m[i]<<' ';
		// cout<<'\n';

		result+=m[a]/P;m[a]%=P;
		if(P==4){
			result+=(m[2])/2;m[2]%=2;
		}
		// cout<<result<<' '<<m[0]<<' '<<m[1]<<'\n';
		for(int i=1;i<P;i++)
			if(m[i]>0){
				result++;break;
			}
		cout<<"Case #"<<cn<<": "<<result<<'\n';
	}
	
	return 0;
}