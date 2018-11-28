/*input
1
3 4
??ED
?C??
???D
*/
#include <bits/stdc++.h>
#define endl '\n'
#define fo(i,n) for(i=0;i<n;++i)
#define forr(i,n) for(i=n-1;i>=0;--i)
using namespace std;
typedef long long int ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;


int pos[26][4];
char a[30][30];

bool check(int x, int y, char c){
	int p = c - 65;
	int i, j;

	int temp0 = pos[p][0];
	int temp1 = pos[p][1];
	int temp2 = pos[p][2];
	int temp3 = pos[p][3];
	if(x < pos[p][0])pos[p][0] = x;
	if(x > pos[p][2])pos[p][2] = x;
	if(y < pos[p][1])pos[p][1] = y;
	if(y > pos[p][3])pos[p][3] = y;

	for(i=pos[p][0];i<=pos[p][2];i++){
		for(j=pos[p][1];j<=pos[p][3];j++){
			if(a[i][j]==c || a[i][j]=='?')
				continue;
			else{
				pos[p][0] = temp0;
				pos[p][1] = temp1;
				pos[p][2] = temp2;
				pos[p][3] = temp3;
				return false;
			}
		}
	}
	
	for(i=pos[p][0];i<=pos[p][2];i++){
		for(j=pos[p][1];j<=pos[p][3];j++){
				a[i][j] = c;
		}
	}

	return true;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);
	ifstream cin("A-large.in");
	ofstream cout("largeA.txt");
	int t;
	cin>>t;
	for(int te=1;te<=t;te++){
		cout<<"Case #"<<te<<":"<<endl;
		int i, j, k, r, c;
		cin>>r>>c;
		vector<char>final;
		fo(i,r)
			fo(j,c)
				cin>>a[i][j];
		for(k=65;k<=91;k++){
			int firstx, firsty, lastx, lasty;
			bool flag = false;
			for(i=0;i<r;i++){
				for(j=0;j<c;j++){
					if(a[i][j]==char(k) && flag==false){
						firstx = i;
						firsty = j;
						lastx = i;
						lasty = j;
						flag = true;
						pos[k-65][0] = firstx;
						pos[k-65][1] = firsty;
						pos[k-65][2] = lastx;
						pos[k-65][3] = lasty;
					}
					else if(a[i][j]==char(k)){
						if(i<firstx)firstx = i;
						if(j<firsty)firsty = j;
						if(i>lastx)lastx = i;
						if(j>lasty)lasty = j;
						pos[k-65][0] = firstx;
						pos[k-65][1] = firsty;
						pos[k-65][2] = lastx;
						pos[k-65][3] = lasty;
					}
				}
			}
			if(!flag)
				continue;
			final.push_back(char(k));
			for(i=firstx;i<=lastx;i++){
				for(j=firsty;j<=lasty;j++){
					a[i][j] = char(k);
				}
			}
		}

		
		fo(i,r){
			fo(j,c){
				if(a[i][j]=='?'){
					for(k=0;k<final.size();k++){
						if(check(i,j,final[k])){
							break;
						}
					}
				}
			}
		}
		fo(i,r){
			fo(j,c)
				cout<<a[i][j];
			cout<<endl;
		}
	}
	return 0;
}
