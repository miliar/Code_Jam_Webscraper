#include<stdio.h>
#include<string.h>
#define SIZE 1005
using namespace std;

char S[SIZE], tmp_[SIZE];
int flp_;
int match_(char t[SIZE]){
	int plus_count = 0;
	//int min_count = 0;
	for(int i = 0 ; i < strlen(t) ; i++)
	{
		if(t[i] == '+')
			plus_count++;
	}
	//printf("%d\n",plus_count);
	if(plus_count == strlen(t))
		return 1;
	else return 0;
}

void flip (int start){
	for (int st = start ; st < start + flp_ ; st++){
		if(tmp_[st] == '+')
			tmp_[st] = '-';
		else tmp_[st] = '+';
	}

}

int main(){
	int n, m, tst_, res = 0, res_found = 0;
	FILE *fp, *fp2;
	fp = freopen("A-large.in","r",stdin);

	scanf("%d", &n);
	tst_ = 1;
	while(tst_ <= n){
	    res = 0;
	    res_found = 0;
		scanf("%s %d", &S, &flp_);
		strcpy(tmp_,S);
		if(match_(S) == 1){
		    res = 0;
		    res_found = 1;
		}
		else{
            for(int pro = 0; pro + flp_ <= strlen(tmp_) ; pro++){
                match_(S);
                if(tmp_[pro] == '-'){
                    flip(pro);
                    res++;
                    if(match_(tmp_) == 1){
                        res_found = 1;
                        break;
                    }
                }
            }
		}
		fp2 = freopen("A-large.out","a",stdout);
        if(res_found)
                printf("Case #%d: %d\n",tst_,res);
            else printf("Case #%d: IMPOSSIBLE\n",tst_);
        tst_++;
    }
    fclose(fp2);
    fclose(fp);
	return 0;

}
