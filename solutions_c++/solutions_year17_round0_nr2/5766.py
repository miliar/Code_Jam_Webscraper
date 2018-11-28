#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 100;

char scan[MAX];
int num[MAX];

int main(){
    int t;
    int len;

    scanf("%d",&t);

    for(int kk=0;kk<t;kk++){
	bool flag = false;

	scanf(" %s",scan);

	len = strlen(scan);

	for(int i=0;i<len;i++) num[i+1] = scan[i] - '0';

	num[len+1] = 987987987;
	num[0] = 987987987;
	
	printf("Case #%d: ",kk+1);

	for(int i=1;i<=len;i++){
	    if(num[i] > num[i+1]) {
		flag = true;
		int thres = -1;

		for(int j=i;j>=0;j--) {
		    if(num[j] == num[j-1]) num[j] = 9;
		    else{
			num[j]--;
			thres = j;
			break;
		    }
		}

		for(int j=thres+1;j<=len;j++) num[j] = 9;

		int j;

		for(j=1;j<=len;j++) {
		    if(num[j] != 0) 
			break;
		}


		if(j == len+1) printf("0");
		else {
			for(;j<=len;j++)
			    printf("%d",num[j]);
		}

		printf("\n");

		break;
	    }
	}

	if(!flag) {
	    for(int i=1;i<=len;i++) printf("%d",num[i]);
	    printf("\n");
	}
    }

    return 0;
}
