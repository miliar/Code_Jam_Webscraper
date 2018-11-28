#include <stdio.h>
#include <sstream>
#include <string>
#include <iostream>

using namespace std;
void flip(string& s,int i){
	if(s[i]== '+'){ s[i]= '-';}
	else if(s[i]== '-'){ s[i]= '+';}
}
int main(){
	int d = 0,m=0,count=0,i=0;
	scanf("%d",&d);
	string vs[d];
	int k[d];
	for(int i = 0;i<d;i++){
		getline(std::cin,vs[i],' ');
		scanf("%d",&k[i]);
	}
	for(auto s : vs){
		count = 0;
		m=s.size();

		for(int j= 0; j<=m-k[i];j++){
			if(s[j] == '-'){
				for(int y=j;y<j+k[i];y++){
					flip(s,y);
				}
				count++;
			}

		}
		int a = (s.find('-'));
		i++;
		if(a>0){ printf("Case #%d: IMPOSSIBLE\n",i);}
		else {printf("Case #%d: %d\n",i,count);}
	}


return 0;
}
