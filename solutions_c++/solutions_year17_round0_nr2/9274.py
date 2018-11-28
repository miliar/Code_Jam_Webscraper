#include<stdio.h>
#include<string.h>
#include<math.h>
#include<stdlib.h>
#include <string>


#define SIZE 20
using namespace std;
char str[SIZE],tem[SIZE];

bool asc(char tmp[SIZE]){
	int trueVal = 1;
	for(int id = 0 ; id < strlen(tmp)-1 ; id++)
	{
		if(tmp[id] > tmp[id+1])
		{
			trueVal = 0;
			break;
		}
	}
	if(trueVal == 1)
		return true;
	else return false;
}

int main(){
	int n, tst_, num , len,number;
	FILE *fp, *fp2;
	fp = freopen("B-small-attempt0.in","r",stdin);
	fp2 = freopen("B-small-attempt0.out","a",stdout);
	//char hello[3];
	scanf("%d",&n);
	tst_ = 1;
	while(tst_ <= n){
		//int res = 0;
	    scanf("%d",&num);
	    //len = log(num) - 1;
	    sprintf(str,"%d",num);
	    strcpy(tem,str);
	    if(strlen(str) == 1) {printf("Case #%d: %d\n",tst_,num); tst_++;}
	    else if(asc(str) == true){
	        //printf("*****");
	        int get = atoi(str);
	        printf("Case #%d: %d\n",tst_,get);
	        tst_++;
	    }
	    else{
	        //printf("*****");
	    	for(int ii = 1; ii <= 100 ; ii++)
	    	{
	    		number = num - ii;
	    		//len = log(number) - 1;
	    		sprintf(tem,"%d",number);
	    		if(asc(tem) == true)
	    			//res = 1;
	    			break;
	    	}
	    	int get = atoi(tem);
	    	printf("Case #%d: %d\n",tst_,get);
	    	tst_++;
	    }
    }
    fclose(fp);
    fclose(fp2);
	return 0;
}

