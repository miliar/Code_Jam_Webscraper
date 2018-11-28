#include <iostream>
#include <cstdio>  
#include <iostream>  
#include <string>  
#include <iterator>  
#include <algorithm>  
#include <vector>  
#include <cstring>  
#include <array>  
#include <queue>  
#include <set>  
#include <map>  
using namespace std;


void solve(char val[]) {
    int end = strlen(val)-1;
    int i;
    while(end != 0) {
        for(i=0;i<end;i++) {
            if(val[i] > val[i+1]) {
                val[i] -= 1;
                for(int j=i+1;j<=end;j++)
                    val[j] = '9';
                break;
            }
        }
        if(i==end)
            end = 0;
        else
            end = i;
    }
}

int main()  
{  
    freopen("B-large.in.txt", "r", stdin);  
    //freopen("in.txt", "r",stdin);  
    freopen("out.txt", "w", stdout);  
    int t;  
    scanf("%d", &t);  
    for (int i = 1; i<= t; i++)  
    {  
        char val[20] = {0};
        cin>>val;
        printf("Case #%d: ", i);  
        solve(val);
        int k = 0;
        while(val[k] == '0')k++;
        for(;k<strlen(val);k++)
            cout<<val[k];
        cout<<endl;
    }  
    return 0;  
}  