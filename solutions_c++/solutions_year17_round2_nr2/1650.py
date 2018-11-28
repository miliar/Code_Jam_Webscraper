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
	int t;
	int N,R,O,Y,G,B,V;
	cin>>t;
	repn(test,1,t){
		cin>>N>>R>>O>>Y>>G>>B>>V;
		vector<pair<int,string> > myvec;
		myvec.push_back(mp(R,"R"));
		myvec.push_back(mp(O,"O"));
		myvec.push_back(mp(Y,"Y"));
		myvec.push_back(mp(G,"G"));
		myvec.push_back(mp(B,"B"));
		myvec.push_back(mp(V,"V"));

		sort(myvec.begin(),myvec.end(),greater<pair<int,string> >());

		int a=myvec[0].first;
		int b=myvec[1].first;
		int c=myvec[2].first;

		string str1=myvec[0].second+myvec[1].second+myvec[2].second;
		string str2=myvec[0].second+myvec[1].second;
		string str3=myvec[0].second+myvec[2].second;

		printf("Case #%d: ",test);
		
		if(a>b+c)
			cout<<"IMPOSSIBLE"<<endl;
		else{
			int count1=b+c-a;
			int count2=b-count1;
			int count3=c-count1;
			for(int i=0;i<count1;i++)
				cout<<str1;

			for(int i=0;i<count2;i++)
				cout<<str2;

			for(int i=0;i<count3;i++)
				cout<<str3;

			cout<<endl;
		}





	}

	return 0;
}

