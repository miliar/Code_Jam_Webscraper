#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>

using namespace std;


int main()
{
    freopen( "A-large.in", "r", stdin );
	freopen( "output.out", "w", stdout );
	int T,n;
	string s;
	scanf("%d\n", &T);
	for(int t = 1; t <= T; t++)
	{
		//fprintf(stderr, "Cas %d\n", t);
		printf("Case #%d: ", t);
		cin>>s>>n;
		char encours = '+';
		int count = 0,f=0;
		int d=s.size();
		for(int i = 0; i < s.size(); i++)
		{

			if(s[i] != encours){
                if(i+n<=d){
                for(int j=0;j<n;j++){
                    if(s[i+j]=='-'){
                        s.replace(i+j,1,"+");
                    }
                    else{
                        s.replace(i+j,1,"-");
                    }
                }
                count++;
			}
			else{
                cout<<"IMPOSSIBLE"<<endl;
                f=1;
                break;
			}
			}
		}
		if(f==0){
		printf("%d\n", count);
		}
	}
	return 0;
}
