#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int arr[20];
int main() {
   
    freopen( "B-large.in", "r", stdin );
	freopen( "B_large_output.txt", "w", stdout );
	int t;
        scanf("%d", &t);
	for (int j = 1; j <= t; j++) 
        {
		char s[20];
                scanf("%s", &s);
		for (int i = 0; i < strlen(s); i++) 
                    arr[i] = s[i]-'0';
		for (int i = 0; i < strlen(s) - 1; i++) 
                {
			if (arr[i] > arr[i + 1]) 
                        {
				arr[i] -= 1;
				for (int j = i + 1; j < strlen(s); j++)    
					arr[j] = 9;
				
				i = -1;
			}
		}
		int i= 0;
		while (arr[i] == 0) 
                    i++;
		printf("Case #%d: ", j);
		for (int k=i; k < strlen(s); k++) 
                    printf("%d", arr[k]);
		printf("\n");
	}
} 