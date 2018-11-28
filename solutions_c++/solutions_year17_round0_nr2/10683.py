#include <iostream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

void checkAss(int digit,int i)
{
    int a[10];
    int val = digit;
    int ans = digit;
    int k = 0;
    int count = 0;
    int b = i;
    while(val != 0)
    {
        a[k] = val%10;
        val = val/10;
        k++;
    }
    for (int j=0;j<k-1;j++)
    {
        if(a[j] >= a[j+1])
        {
            count++;
        }
    }
    if(k > 1)
    {
    if(count == k-1)
    {
        printf("Case #%d: %d\n",i,ans);
    }
    else
    {
        checkAss(ans-1,b);
    }
    }
    else
    {
      printf("Case #%d: %d\n",i,ans);
    }
}

int main() 
{
	int t;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d",&t);
    for (int i=0;i<t;i++)
    {
   	int digit;
   	scanf("%d",&digit);
   checkAss(digit,i+1);
    }
}
