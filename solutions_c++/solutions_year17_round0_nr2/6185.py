#include <iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("temp_big.out","w",stdout);
    int t;
    int test=0;
    scanf("%d",&t);
    while(t--)
    {
        test++;
        long long n;
        scanf("%lld",&n);
        long long temp=n;
        stack<int> st;
        while(temp)
        {
            st.push(temp%10);
            temp/=10;
        }
        int i=0;
        int siz=0;
        int arr[21];
        while(!st.empty())
        {
            siz++;
            arr[i]=st.top();
            st.pop();
            i++;
        }
        long long new_num=1,num;
        int prev,bac=siz-1;
        int ne[21];
        bool break_flag=false;
        for(int i=1;i<siz;i++){
            new_num*=10;
            new_num++;
        }
        //printf("new_num=%lld\n",new_num);
        if(n<new_num)
        {
            num=9;
            for(int i=1;i<siz-1;i++){
                num*=10;
                num+=9;
            }
            printf("Case #%d: %lld\n",test,num);
        }
        else
        {
            prev=arr[0];
            ne[0]=arr[0];
            for(int i=1;i<siz;i++)
            {
                if(break_flag==true)
                    break;

                if(arr[i]>=prev){
                    ne[i]=arr[i];
                    prev=ne[i];
                }
                else
                {
                    bac=i-1;
                    //printf("ne[bac]=%d ne[bac-1]=%d\n",ne[bac],ne[bac-1]);
                    if(ne[bac]>ne[bac-1])
                    ne[bac]--;
                    else
                    {
                        while(ne[bac-1]==ne[bac] && bac-1>=0)
                            bac--;
                        if(bac==1 && ne[bac]==ne[bac-1])
                        {
                            bac--;
                            ne[bac]--;
                        }
                        else
                            ne[bac]--;
                    }
                    break_flag=true;
                }
            }
            //printf("bac=%d\n",bac);
            for(int i=bac+1;i<siz;i++)
                ne[i]=9;
                printf("Case #%d: ",test);
            for(int i=0;i<siz;i++)
                printf("%d",ne[i]);
            printf("\n");
        }

    }
    return 0;

}
