#include<bits/stdc++.h>
using namespace std;
#define MOD 1000000007
#define INF INT_MAX/2
#define PI 3.14159265358979323846264338327950
#define reset(a,x) memset(a,x,sizeof(a))

#define ll long long
#define ull unsigned long long
#define ii pair<int,int>
#define vi vector<int> 
#define vii vector<ii>
#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define all(c) (c).begin,(c).end()
#define tr(c,i) for(typeof((c).begin() i = (c).begin(); i != (c).end(); i++) 
#define rep(a,b,c)   for(int (a)=(b); (a)<(c); (a)++)
#define repn(a,b,c)  for(int (a)=(b); (a)<=(c); (a)++)
#define repd(a,b,c)  for(int (a)=(b); (a)>=(c); (a)--)

int moves[8][2]={{-1,0},{1,0},{0,1},{0,-1},{1,1},{-1,-1},{-1,1},{1,-1}};
bool issafe(int i,int j){
    return (i>=0 && i<8 && j>=0 && j<8);
}

int main(){
	int t,k;
	string S;
	cin>>t;
	repn(test,1,t){
		cin>>S>>k;
		bool possible=1;
		int count=0;
		int n=S.length();
		for (int i=0;i<n;i++){
			if(S[i]=='-'){
				count++;
				if(i+k>n){
					possible=false;
					break;
				}
				for(int j=i;j<i+k;j++)
					S[j]=(S[j]=='+'?'-':'+');
			}
		}

		printf("Case #%d: ",test);
		if(possible)
			cout<<count<<endl;
		else
			cout<<"IMPOSSIBLE"<<endl;
	}

	return 0;
}

