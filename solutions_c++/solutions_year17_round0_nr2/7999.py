#include <cstdio>
#include <cstring>

using namespace std;

char cad[30];
int tc;
bool cambio;

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &tc);
    for(int t=1; t<=tc; t++)
    {
        scanf("%s", cad);

        //do{
            cambio = false;
            for(int i=strlen(cad)-1; i>0; i--)
            {
                if(cad[i]<cad[i-1])
                {
                    cambio = true;
                    cad[i-1] = cad[i-1]-1;
                    for(int j=i; j<strlen(cad); j++)
                        cad[j] = '9';
                }
            }
        //}while(cambio);

        int pos = 0;
        while(cad[pos] == '0') pos++;
        printf("Case #%d: ", t);

        for(int i=pos; i<strlen(cad); i++) printf("%c", cad[i]);

        printf("\n");

    }
    return 0;
}
