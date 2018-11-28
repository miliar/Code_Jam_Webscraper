#define LLI long long int
#include <stdio.h>
#include <math.h>

long long int k,n;

void proceso(){
	LLI niv = floor(log2(k));
	LLI ksim = (1 << niv)-1;
	LLI sobran = k - ksim;
	LLI espacios = ksim+1;
	LLI tamEspacio = (n-ksim)/(espacios);
	LLI espaciosGrandes = (n-ksim)%(espacios);
	if(sobran <= espaciosGrandes)
		tamEspacio++;
	if(tamEspacio % 2 == 0)
		printf("%lld %lld\n",tamEspacio/2,(tamEspacio-1)/2);
	else
		printf("%lld %lld\n",tamEspacio/2,tamEspacio/2);
}
int main(){
	freopen("in","r",stdin);
	int t;
	scanf("%d",&t);
	for(int i = 1; i <= t;i++){
		scanf("%lld %lld",&n,&k);
		printf("Case #%d: ",i);
		proceso();
	}
	return 0;
}
