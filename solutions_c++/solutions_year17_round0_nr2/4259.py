#include <cstdio>
#include <cstring>


using namespace std;

char ciag[20];
int ile, dl;

bool sprawdz(){
	for(int j=1; j<dl; j++){
		if(ciag[j]<ciag[j-1]){
			return false;
		}
	}
	return true;
}

void napraw(){
	for(int j=1; j<dl; j++){
		if(ciag[j]<ciag[j-1]){
			ciag[j-1]--;
			for(int g=j; g<dl; g++){
				ciag[g]='9';
			}
		}
	}
}

int main(){
	scanf("%d", &ile);
	for(int i=0; i<ile; i++){
		printf("Case #%d: ", i+1);
		for(int j=0; j<20; j++){
			ciag[j] = '\0';
		}
		scanf("%s", ciag);
		dl = strlen(ciag);
		while(!sprawdz()){
			napraw();
		}
		for(int g=0; g<dl; g++){
			if(ciag[g]!='0')
				printf("%c", ciag[g]);
		}
		printf("\n");
	}

}
