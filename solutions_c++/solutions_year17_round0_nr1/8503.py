#include<iostream>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
int main(){
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
int t;
std::cin>>t;
int q=t;
while(q--){
int k;
	std::string str;
	std::cin>>str;
        std::cin>>k;
        int count=0;
	//int i_dec = atoi(str1.c_str());
	int len =str.size();
        for(int i=0;i<len-k+1;i++){
            if(str[i]=='-'){
              for(int j=i;j<i+k;j++){
                  if(str[j]=='-')
                    str[j]='+';
                   else
                    str[j]='-';
             }
            count++;
			}
		}
		int x=0;
		for(int i=0;i<len;i++){
			if(str[i]=='-')
				x=1;
		}
		int y=t-q;
		if(x==0)
			std::cout<<"Case #"<<y<<": "<<count<<"\n";
        //std::cout<<count;
	else
		std::cout<<"Case #"<<y<<": IMPOSSIBLE"<<"\n";


}
}
