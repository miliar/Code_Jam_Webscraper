#include<stdio.h>
#include<algorithm>
using namespace std;

struct es{
	int izq;
	int der;
	bool hay;
}arr[1000+10],aux;

int ind,n,k,t;

int main(){
    freopen("C-small-1-attempt0.in","r",stdin);
	freopen("salida.out","w",stdout);
	scanf("%d",&t);
	for(int c=1;c<=t;c++){
        scanf("%d%d",&n,&k);
        arr[0].hay=true;
        arr[n+1].hay=true;
        for(int i=1;i<=k;i++){
            aux.der=-1;
            aux.izq=-1;
            for(int j=1;j<=n;j++){
                if(arr[j].hay) continue;
                arr[j].der=arr[j].izq=0;
                for(int h=j+1;h<=n&&!arr[h].hay;h++) arr[j].der++;
                for(int h=j-1;h>=1&&!arr[h].hay;h--) arr[j].izq++;
                if(min(arr[j].der,arr[j].izq)>min(aux.der,aux.izq)){
                    aux=arr[j];
                    ind=j;
                }else if(min(arr[j].der,arr[j].izq)==min(aux.der,aux.izq)&&max(arr[j].der,arr[j].izq)>max(aux.der,aux.izq)){
                        aux=arr[j];
                        ind=j;
                }
            }
            arr[ind]=aux;
            arr[ind].hay=true;
        }
        for(int i=0;i<=n+1;i++) arr[i].der=arr[i].izq=arr[i].hay=0;
        printf("Case #%d: %d %d\n",c,max(aux.der,aux.izq),min(aux.der,aux.izq));
	}
	fclose(stdout);
}
