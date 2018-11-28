#include<bits/stdc++.h>
using namespace std;
#define fori(a,b) for(lli (i)=(lli)(a);(i)<=(lli)(b);(i)++)
#define forj(a,b) for(lli (j)=(lli)(a);(j)<=(lli)(b);(j)++)
#define fork(a,b) for(lli (k)=(lli)(a);(k)<=(lli)(b);(k)++)
#define pb push_back
#define mp make_pair
#define f first
#define s second
#define inf 1000000007
#define pi 3.14159265359
#define fastio ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define sz(a) (lli)(a).size()
#define iter(a) typeof((a).begin())
typedef long long int lli;
typedef vector< lli > vlli;
typedef pair<lli,lli> plli;
typedef set<lli> slli;
typedef map<lli,lli> mlli;



int main()
{
	int t,n,r,k,R,O,Y,G,B,V;
	cin>>t;
	

	r=t;
	while(t--){
		
		cin>>n;
		cin>>R>>O>>Y>>G>>B>>V;
		
		int flag=0;
		int B1=0;
		int R1=0;
		int Y1=0; 
		
		if(R+G+Y+V==0||B+O+Y+V==0||R+G+B+O==0){

			if(B!=O||R!=G||Y!=V)
			flag=1;
			if(B!=0)
			B1=1;
			if(R!=0)
			R1=1;
			if(Y!=0)
			Y1=1;
		}	
		
		else{
			if((B<O+1&&O!=0)||(R<G+1&&G!=0)||(Y<V+1&&V!=0))
			flag=1;

			B1=B-O;
		 	R1=R-G;
			Y1=Y-V;
		}

		

		if(flag==1){
			cout<<"Case #"<<r-t<<": "<<"IMPOSSIBLE"<<endl;
		}
		else{

			priority_queue<pair<int,int> >rr;

			rr.push({B1,0});
			rr.push({R1,1});
			rr.push({Y1,2});

			pair<int,int> a1=rr.top();
			rr.pop();
			pair<int,int> a2=rr.top();
			rr.pop();
			pair<int,int> a3=rr.top();
			rr.pop();

			if(a1.f>a2.f+a3.f&&a2.f+a3.f!=0){

				cout<<"Case #"<<r-t<<": "<<"IMPOSSIBLE"<<endl;
				continue;
			}

			int yy;
			if(a2.f+a3.f!=0)
				yy=(a2.f+a3.f)-a1.f;
			else
				yy=1;
			//cout<<yy<<"h"<<endl;
			vector<int> v;

			for(int i=1;i<=yy;i++){
				v.push_back(a1.s);
				if(a2.f!=0){
					v.push_back(a2.s);
					a2.f--;
				}
				if(a3.f!=0){
					v.push_back(a3.s);
					a3.f--;
				}

			}

			while(a2.f!=0){
				v.push_back(a1.s);
				v.push_back(a2.s);
				a2.f--;
			}
			while(a3.f!=0){
				v.push_back(a1.s);
				v.push_back(a3.s);
				a3.f--;
			}

			

			int b1=0;
			int b2=0;
			int b3=0;
			cout<<"Case #"<<r-t<<": ";
			if(0){

			}
			else{
				for(int i=0;i<v.size();i++){
					if(v[i]==0&&b1==0){
						for(int j=1;j<=O;j++){
							cout<<"BO";
						}
						if(v.size()!=1)
						cout<<"B";
						b1=1;
					}
					else if(v[i]==0){
						cout<<"B";
					}
					if(v[i]==1&&b2==0){
						for(int j=1;j<=G;j++){
							cout<<"RG";
						}
						if(v.size()!=1)
						cout<<"R";
						b2=1;
					}
					else if(v[i]==1){
						cout<<"R";
					}
					if(v[i]==2&&b3==0){
						for(int j=1;j<=V;j++){
							cout<<"YV";
						}
						if(v.size()!=1)
						cout<<"Y";
						b3=1;
					}
					else if(v[i]==2){
						cout<<"Y";
					}
				}
			}
			cout<<endl;
			

		}

		
	}

	return 0;
}