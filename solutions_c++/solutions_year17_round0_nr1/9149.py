#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string.h>
#include <map>
#include <set>
#include <deque>
#include <math.h>

using namespace std;
int main (){
string s;
int t,n,i,j,f=0,c=1,l,flag;
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
cin>>t;
while(t--){
    i=0;
	f=0;
	flag=1;
    cin>>s>>n;
    printf("Case #%d: ",c++);
	l=s.size();
	
	char ch[l];
	memset(ch,'+',l);
	if(s==ch){
		printf("0\n");
		continue;
		}
	while(i!=l){
		if(s[i]=='+'){
			i++;
		}
		else{
			s[i++]='+';
			if(i+n-1 > l){
						cout<<"IMPOSSIBLE\n";
						flag=0;
						break;

			}
			for(j=i;j<i+n-1;j++){
				s[j]=(s[j]=='+')?'-':'+';
			}
			f++;
		}
	}
	if(flag){
	printf("%d\n",f);
	}
}


return 0;


}
