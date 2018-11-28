#include<bits/stdc++.h>
#define lli long long int
#define test()  int test;cin>>test;while(test--)
const lli MOD = 1000000007ll;

using namespace std;

int main() {
  	freopen("in", "r", stdin);
  	freopen("out", "w", stdout);
	std::ios_base::sync_with_stdio(false);
  	int tt;
  	cin >> tt;
  	for (int qq = 1; qq <= tt; qq++) {
    	cout << "Case #" << qq << ": "<<endl;;
    	int r,c;
    	cin >> r >> c;
    	string st[r];
    	for(int i=0;i<r;i++){
    	    cin >> st[i];
    	}
    	int r1=0;
    	for(int i=0;i<r;i++){
    	    int c1=0;
    	    char pre = 'c';
    	    for(int j=0;j<c;j++){
    	        if(st[i][j]!='?'){
    	            for(int x=r1;x<=i;x++){
    	                for(int y=c1;y<=j;y++){
    	                    st[x][y] = st[i][j];
    	                }
    	            }
    	          //  r1=i+1;
    	            c1=j+1;
    	            pre = st[i][j];
    	        }
    	        else if(j==c-1 && pre!='c'){
    	            for(int x=r1;x<=i;x++){
    	                for(int y=c1;y<=j;y++){
    	                    st[x][y] = pre;
    	                }
    	            }
    	        }
    	    }
    	    if(pre!='c'){
    	        r1 = i+1;
    	    }
    	    if(pre=='c' &&i==r-1){
    	        for(int x=1;x<r;x++){
    	            for(int y=0;y<c;y++){
    	                if(st[x][y]=='?'){
    	                    st[x][y] = st[x-1][y];
    	                }
    	            }
    	        }
    	    }
    	}
    	for(int i=0;i<r;i++){
    	    for(int j=0;j<c;j++){
    	        cout << st[i][j] ;
    	    }
    	    cout << endl;
    	    
    	}
    }
  return 0;
}
