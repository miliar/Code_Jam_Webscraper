#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int mystrlen(char s[])
{
    int i=0;
    while(s[i]!='\0')
        i++;
    return i;
}
int func(char s[],int j)
{
    int i=0;
    while(i+1 <= j)
    {
        if(s[i]!=s[i+1])
            return 0;
            i++;
    }
    return 1;
}

int main()
{
   // freopen("B-small-attempt0.in","r",stdin);
   // freopen("outputbadhon.txt","w+",stdout);
    int n,k,len,f;
    int i,j;

    cin >> n;
    i=0;
    char str[30];
    int tmp;
    while(i<n)
    {
        cin >> str;
        len = mystrlen(str);
        f=1;
        for(j=0; j<len; j++)
        {
            if(f==0)
                str[j] = 57;
            if(str[j] > str[j+1] && f==1 && j+1<=len-1)
            {
                tmp = func(str,j);
                if(tmp==1)
                {
                    str[0]--;
                    j=0;

                }
                else{
                str[j]--;

                }
                f=0;
            }

        }

        if(str[0]==48)
        {
            cout << "Case #" << i+1 << ": ";
            for(k=1; k<len; k++)
                cout << str[k];
            cout<<endl;
        }
        else
        cout << "Case #" << i+1 << ": " << str << endl;

        i++;
    }
    return 0;
}
