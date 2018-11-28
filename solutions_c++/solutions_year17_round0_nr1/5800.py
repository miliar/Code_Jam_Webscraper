#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX = 1005;

char scan[MAX];
int len;
int sz;

bool check(int inx) {
    char a = scan[inx];

    for(int i=inx+1;i<len;i++){
	if(scan[i] != a)
	    return false;
    }

    return true;
}

void flip(int inx){
    for(int i=inx;i<inx+sz;i++){
	scan[i] = scan[i] == '+' ? '-' : '+';
    }
}

int main(){
    int t;

    scanf("%d",&t);

    for(int k=0;k<t;k++){
	int result = 0;

	scanf(" %s %d",scan, &sz);

	len = strlen(scan);

	if(len < sz){
	    if(scan[0] == '+' && check(0)) {
		result = 0;
	    }
	    else result = -1;
	}
	else {
	    int endPoint = len - sz + 1;

	    for(int i=0;i<endPoint;i++){
		if(scan[i] == '-') {
		    flip(i);
		    result++;
		}
	    }

	    if(!(scan[endPoint] == '+' && check(endPoint))) 
		result = -1;
	}

	printf("Case #%d: ",k+1);

	if(result == -1) printf("IMPOSSIBLE\n");
	else printf("%d\n",result);
    }

    return 0;
}
