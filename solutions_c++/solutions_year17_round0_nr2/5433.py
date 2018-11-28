#include <iostream>
#include <string.h>
#include <vector>
#include <stdio.h>
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false);
    long long int t;
    cin>>t;
    int j;
    for(j=0;j<t;j++)
    {
    	char n[20];
    	vector <int> a;
        cin>>n;
        for(long long int i=0;i<strlen(n);i++){
        	a.push_back(n[i]-'0');
        }
        for(long long int i=0;i<strlen(n)-1;i++){
            if(a[i]>a[i+1]){
               a[i]--;
               int temp=i+1;
               while(temp<strlen(n)){
               		a[temp]=9;
                	temp+=1;
               }
                temp=i;
                while(temp>0 && a[temp]<a[temp-1]){
            	    a[temp]=9;
                    a[--temp]--;
                }
            }
        }
        printf("Case #%d: ",j+1);
        for(long long int i=0;i<strlen(n);i++)
        if(a[i]!=0)
            printf("%d",a[i]);
        printf("\n");
    }
    return 0;
}