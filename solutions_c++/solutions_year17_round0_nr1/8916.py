#include <iostream>
#include<stdio.h>
#include<string.h>
using namespace std;
   char s[10000];

int main()
{
    FILE *f,*f2;
     f=fopen("test.txt","r");
    f2=fopen("test2.txt","w");
    int n;
    fscanf(f,"%d",&n);
    cout<<n;
    for(int l=1;l<=n;l++)
    {
        int k;
        int count1=0;
        fscanf(f,"%s",s);
        cout<<s;
        fscanf(f,"%d",&k);
        cout<<k;
        int i;
        for(i=0;i<strlen(s)-k;i++)
        {

            if(s[i]=='+')
               {
                 cout<<"Plus\n";
                 continue;
               }
            else
            {
                count1++;
                cout<<"count1="<<count1<<"\n";
                for(int j=i;j<k+i;j++)
                {
                    if(s[j]=='-')
                    {
                        s[j]='+';
                        cout<<'+';
                    }
                    else
                    {
                        s[j]='-';
                        cout<<'-';
                    }
                }
            }
        }
        int count2=0,count3=0;
        while(i<strlen(s))
        {
            if(s[i]=='+')
                {count2++;
                i++;
                cout<<"1Plus\n";}
            else
                {count3++;
                i++;
                cout<<"1minus\n";}

        }
        if(count2==k)
            fprintf(f2,"Case #%d: %d\n",l,count1);
        else if(count3==k)
            fprintf(f2,"Case #%d: %d\n",l,count1+1);
        else
            fprintf(f2,"Case #%d: IMPOSSIBLE\n",l);
    }
    return 0;
}
