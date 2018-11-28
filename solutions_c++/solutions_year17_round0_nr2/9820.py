#include <iostream>
#include <stdio.h>
using namespace std;

long checktidy(char* a)
{
    int pastInt[19];
    pastInt[0] = -1;
    char* head = a;
    int n=1;
    int c = 1;
    long i;
    //int i;
     while(*a != '\0')
    {
        if(*a-'0'>= pastInt[n-1])
        {
            pastInt[n] = *a-'0';
            n++;
            a++;
        }else
        {
            n--;
            char* save = a;
            a--;
            while(a != head)
            {
                if(pastInt[n] == pastInt[n-1])
                {
                    *a = '9';
                }else{
                    break;
                }
                a--;
                n--;
                //pastInt--;
                //a--;
                //char b[1];
                //sprintf(b,"%d", pastInt);
                //*a = *b;
                //a--;
            }
            pastInt[n]--;
            char b[1];
            sprintf(b,"%d", pastInt[n]);
            *a = *b;
            while(a != save)
            {
                a++;
            }
            //a++;
            while(*a != '\0')
            {
                *a = '9';
                a++;
            }
            c = 0;
            break;
        }
        
    }
    if(c == 0)
    {
        sscanf(head, "%ld", &i);
        return i;
    }else{
        sscanf(head, "%ld", &i);
        return i;
    }
}

int main(){
        long i;
        int n;
        scanf("%d",&n);
    for(int j=1;j<=n;j++)
    {
        char a[100];
        scanf("%s",a);
        i = checktidy(a);
        cout << "Case #";
        cout << j;
        cout << ": ";
        cout << i << endl;
        
    }
    
}