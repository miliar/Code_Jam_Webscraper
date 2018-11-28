#include <cstdio>
#include <cstring>

using namespace std;

int sprawdz(char* ciag, int p){
	int licz = 0;
	int dl = strlen(ciag);
	for(int i=0; i<=dl-p; i++){
		//printf("#%d: %s\n", i, ciag);
		if(ciag[i]=='-'){
			licz++;
			for(int j=i; j<i+p; j++){
				ciag[j] = (ciag[j] == '-' ? '+' : '-');
			}
		}
		
	}
	for(int i=dl-p+1; i<dl; i++){
		if(ciag[i]=='-'){
			return -1;
		}
	}
	return licz;
}

int main(){
	int num, p;
	char ciag[1005];
	scanf("%d", &num);
	for(int i=0; i<num; i++){
		for(int j=0; j<1005; j++){
			ciag[j]='\0';
		}
		scanf("%s %d", ciag, &p);
		int wyn = sprawdz(ciag, p);
		if(wyn == -1){
			printf("Case #%d: IMPOSSIBLE\n", i+1);
		}
		else {
			printf("Case #%d: %d\n", i+1, wyn);
		}
	}
	return 0;
}
