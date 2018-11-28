#include <cstdio>
#include <cstring>
#include <cstdlib>

using namespace std;

int tc,num[20];
char arr[100];
bool haypedo;

int main()
{
    freopen("in.in","r",stdin);
    freopen("o.out","w",stdout);
    scanf("%d",&tc);
    for(int k=1;k<=tc;k++)
    {
        printf("Case #%d: ",k);
        scanf("%s",arr);
        bool jaja=false;
        haypedo=false;
        int aux=0;
        int l=strlen(arr);
        for(int i=0;i<l;i++)
        {
            num[i]=arr[i]-'0';
            if(i!=0)
                if(num[i]<num[i-1])
                    jaja=true;
        }
        if(!jaja)
        {
            printf("%s\n",arr);
            continue;
        }
        else
        {
            if(l==1)
            {
                printf("%s\n",arr);
                continue;
            }
            if(arr[0]=='1' && arr[1]=='0')
            {
                for(int i=0;i<l-1;i++)
                    printf("9");
                printf("\n");
            }
            else if(arr[0]=='1') //rebajar ultima unidad
            {
                for(int i=0;i<l;i++)
                    if(num[i]!=0 && num[i]!=1)
                        haypedo=true;
                if(!haypedo) //no hay pedo
                {
                    for(int i=0;i<l-1;i++)
                        printf("9");
                    printf("\n");
                }
            }
            if(haypedo || num[0]!=1) //no rebajar ultima unidad
            {
                bool nueves=false;
                for(int i=0;i<l-1;i++)
                {
                    if(num[i]>num[i+1])
                    {
                        int varaux=num[i],numauxantes;
                        if(num[i-1]==num[i])
                            num[i]=9;
                        else
                            num[i]--;
                        if(i>0)
                            aux=i-1;
                        numauxantes=num[aux];
                        while(num[aux]==varaux)
                        {
                            numauxantes=num[aux];
                            num[aux]=9;
                            if(aux-1>=0)
                                aux--;
                            else
                                break;
                        }
                        if(aux!=0)
                            num[aux+1]=varaux-1;
                        else if(numauxantes==varaux)
                            num[aux]=varaux-1;
                        for(int j=i+1;j<l;j++)
                            num[j]=9;
                        break;
                    }
                }
                for(int i=0;i<l;i++)
                    printf("%d",num[i]);
                    printf("\n");
            }
        }
    }
}
