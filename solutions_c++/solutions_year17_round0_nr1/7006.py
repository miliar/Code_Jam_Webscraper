#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
//#include<cfile>
using namespace std;

int T,k,cnt;
bool flag;
char s[1005];
FILE *fp,*fo;
int main(){
	fp=fopen("A-small-attempt3.in","r");
	fo=fopen("A-small-attempt3.out","w+");
	fscanf(fp,"%d",&T);
	for(int t=1;t<=T;t++){
		flag=true;
		cnt=0;
		fscanf(fp,"%s",s);
		fscanf(fp,"%d",&k);
		for(int i=0;i<strlen(s)-k+1;i++){
			if(s[i]=='-'){
				cnt++;
				for(int j=i;j<i+k;j++){
					s[j]= (s[j]=='-')?'+':'-';	
				}
//				cout<<s<<endl;
			}
		}
		for(int i=strlen(s)-k;i<strlen(s);i++){
			if(s[i]=='-'){
				flag=false;
				fprintf(fo,"Case #%d: IMPOSSIBLE\n",t);
				break;
			}
		}
		if(flag) fprintf(fo,"Case #%d: %d\n",t,cnt);
		
	}
	
	return 0;
} 
