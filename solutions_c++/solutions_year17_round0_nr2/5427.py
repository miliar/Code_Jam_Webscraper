#include <iostream>
#include <string.h>
#include <vector>
#include <stdio.h>
using namespace std;

int main() {
    long long int t;
    cin>>t;
    int jj;
    for(jj=0;jj<t;jj++)
    {
    	char n[20];
    	vector <int> a;
    	int i;
        scanf("%s",n);
        for(i=0;i<strlen(n);i++)
        {
        	a.push_back(n[i]-'0');
        }
        
        // int ee;
        // for(ee=0;ee<strlen(n);ee++)
        // printf("%d ",a[ee]);
        // printf("\n");
        
        for(long long int i=0;i<strlen(n)-1;i++)
        {
            if(a[i]>a[i+1])
            {
               a[i]--;
               int temp=i+1;
               
               while(temp<strlen(n))
               {
               		a[temp]=9;
                	temp+=1;
               }
               
                temp=i;
               
            while(temp>0 && a[temp]<a[temp-1])
            {
            	a[temp]=9;
                a[--temp]--;
               // temp--;
            }
                
            }
            
        }
        printf("Case #%d: ",jj+1);
        for(i=0;i<strlen(n);i++)
        if(a[i]!=0)
            printf("%d",a[i]);
        printf("\n");
    }
    return 0;
}