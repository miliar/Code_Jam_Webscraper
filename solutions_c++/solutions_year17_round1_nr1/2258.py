#include <bits/stdc++.h>
#define endl '\n'
#define ll long long
#define ii piar<int, int>
#define vi vector<int, int>
#define vii vector<pair<int, int>>
#define fi first
#define se second
#define pb push_back
#define mp make_pair

//Language: c++11
//Compiler: g++
//IDE: Code::Blocks

using namespace std;

struct letter{
	int a, b;
	int x1, x2, y1, y2;
	char c;
};

char A[30][30], c;
vector<letter> V;
int S[300];

void update(int y1, int y2, int x1, int x2, char c, int i){
	for(int i=y1; i<=y2; i++){
		for(int j=x1; j<=x2; j++){
			A[i][j]=c;
		}
	}
	V[i].x1=x1;
	V[i].x2=x2;
	V[i].y1=y1;
	V[i].y2=y2;
	S[c]=i;
}

int main()
{
	int t;
	cin>>t;
	for(int k=1; k<=t; k++){
		int n, m;
		cin>>n>>m;
		V.clear();
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				cin>>c;
				if(c!='?'){
					letter a;
					a.c=c;
					a.a=i;
					a.b=j;
					V.pb(a);
				}
			}
		}
		update(0, n-1, 0, m-1, V[0].c, 0);

		for(int i=1; i<V.size(); i++){
			letter& other=V[S[A[V[i].a][V[i].b]]];
			int ind=S[A[V[i].a][V[i].b]];
			if(other.a<V[i].a){
				update(other.a+1, other.y2, other.x1, other.x2, V[i].c, i);
				update(other.y1, other.a, other.x1, other.x2, other.c, ind);
			}
			else if(other.a>V[i].a){
				update(other.y1, other.a-1, other.x1, other.x2, V[i].c, i);
				update(other.a, other.y2, other.x1, other.x2, other.c, ind);
			}
			else if(other.b<V[i].b){
				update(other.y1, other.y2, other.b+1, other.x2, V[i].c, i);
				update(other.y1, other.y2, other.x1, other.b, other.c, ind);
			}
			else{
				update(other.y1, other.y2, other.x1, other.b-1, V[i].c, i);
				update(other.y1, other.y2, other.b, other.x2, other.c, ind);
			}
		}

		cout<<"Case #"<<k<<":\n";
		for(int i=0; i<n; i++){
			for(int j=0; j<m; j++){
				cout<<A[i][j];
			}cout<<endl;
		}
	}
}
