#include <iostream>
#include <stdio.h>
#include <string>
#include <cstring>

using namespace std;
int casos,tama,pos,x;
char cadena[30];
int main()
{
    freopen("i.in","r",stdin);
    freopen("o.out","w",stdout);
   scanf("%d",&casos);
   while(casos--)
   {
       x++;
        pos=0;
       scanf("%s",cadena);

       for(int i=strlen(cadena)-1;i>0;i--)
       {
           if(cadena[i]<cadena[i-1])
           {
               cadena[i-1]=cadena[i-1]-1;
               for (int j=i;j<strlen(cadena);j++)
                cadena[j]='9';
           }
       }
       printf("Case #%d: ",x);
      while (cadena[pos]=='0')pos++;
       for (int i=pos;i<strlen(cadena);i++)
       printf("%c",cadena[i]);
        printf("\n");
   }
}
