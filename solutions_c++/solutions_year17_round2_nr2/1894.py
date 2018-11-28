#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <sstream>
#include <ctime>

char A[1024];

using namespace std;  // since cin and cout are both in namespace std, this saves some text
void main() {
	int T,ct,i,j;
	int N, R, O, Y, G, B, V;
	char c;
	char a[3];
	int n[3];

	//R + Y = O
	//Y + B = G
	//R + B = V

	cin >> T;
//	T=3;
	for (ct = 1; ct <= T; ++ct) {
		cin >>	N; 
		cin >>	R; 
		cin >>	O; 
		cin >>	Y; 
		cin >>	G; 
		cin >>	B; 
		cin >>	V;

		if(R==0 && Y==0){
			cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
			continue;
		}
		if(R==0 && B==0){
			cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
			continue;
		}
		if(B==0 && Y==0){
			cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
			continue;
		}
		if(R==0){
			if(B!=Y){
				cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
				continue;
			}
			else {
				cout << "Case #" << ct <<": ";
				for(i=0;i<B;i++) printf("BY");
				printf("\n");
				continue;
			}
		}
		if(B==0){
			if(R!=Y){
				cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
				continue;
			}
			else {
				cout << "Case #" << ct <<": ";
				for(i=0;i<R;i++) printf("RY");
				printf("\n");
				continue;
			}
		}
		if(Y==0){
			if(B!=R){
				cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
				continue;
			}
			else {
				cout << "Case #" << ct <<": ";
				for(i=0;i<B;i++) printf("BR");
				printf("\n");
				continue;
			}
		}

		if(Y > B+R){
			cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
			continue;
		}
		if(B > Y+R){
			cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
			continue;
		}
		if(R > Y+B){
			cout << "Case #" << ct <<": IMPOSSIBLE"<< endl;
			continue;
		}
		a[0] ='Y'; n[0] = Y;
		a[1] ='B'; n[1] = B;
		a[2] ='R'; n[2] = R;
		if(n[1]>n[0]){
			j = n[1]; n[1] = n[0]; n[0] = j;
			c = a[1]; a[1] = a[0]; a[0] = c;
		}
		if(n[2]>n[1]){
			j = n[1]; n[1] = n[2]; n[2] = j;
			c = a[1]; a[1] = a[2]; a[2] = c;
		}
		if(n[1]>n[0]){
			j = n[1]; n[1] = n[0]; n[0] = j;
			c = a[1]; a[1] = a[0]; a[0] = c;
		}
//		for(i=0;i<3;i++) printf("%c %d\n",a[i],n[i]);


		cout << "Case #" << ct <<": ";
		if(n[0] == n[1]+n[2]){
			for(i=0;i<n[1];i++)
				printf("%c%c",a[0],a[1]);
			for(i=0;i<n[2];i++)
				printf("%c%c",a[0],a[2]);
			printf("\n");
		}
		else {
			if(n[0]==n[1]){
				for(i=0;i<n[2];i++)
					printf("%c%c%c",a[0],a[1],a[2]);
				if(n[1]>n[2]){
					for(i=0;i<n[1]-n[2];i++)
						printf("%c%c",a[0],a[1]);
				}
				printf("\n");
			}
			else {
				for(i=0;i<n[0]-n[2];i++)
					printf("%c%c",a[0],a[1]);
				for(i=0;i<n[1]+n[2]-n[0];i++)
					printf("%c%c%c",a[0],a[1],a[2]);
				for(i=0;i<n[0]-n[1];i++)
					printf("%c%c",a[0],a[2]);
				printf("\n");
			}
		}

	}
}