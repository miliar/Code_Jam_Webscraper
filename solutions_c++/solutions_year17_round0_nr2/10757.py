#pragma warning(disable:4996)
#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<vector>
#include<string.h>
using namespace std;
typedef unsigned long long ULL;

ULL convert(ULL in,ULL *s1) {
    int count = 999;
    int length = 0;
    ULL ret = in;
    while(in) {
        s1[count] = in % 10;
        in = in/10;
        length++;
        count--;
    }
    count = 999;
    for(int i = 0;i< length;i++) {
        if( s1[count]  < s1[count - 1]) {
            return 0;
        }
        count--;
    } 
    return ret;         
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int TC;
        ULL in, result = 0,i;
        ULL s1[1000] = {0};
        int loop = 0;
	scanf("%d", &TC);
	for (int T = 1; T <= TC; T++){
	    scanf("%llu",&in);
            memset(s1,0,(sizeof(ULL) * 1000));
            for(i = in;i>0;i--) 
            {
                result = convert(i,s1);
                if(result) 
                    break;
                memset(s1,0,(sizeof(ULL) * 1000));
            }
	    printf("Case #%d: %llu\n",T,result);
	}
}
