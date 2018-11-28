#include <bits/stdc++.h>
using namespace std;

int n, k, T;

int main()
{
	cin>>T;

for(int t = 1; t <= T; t++) 
{
	priority_queue<int> heap;
	cin>>n>>k;
	heap.push(n);

	for(int i=0;i<k-1;i++)
    {
        	int tamanho_bloco = heap.top();

        	heap.pop();

            if(tamanho_bloco%2!=0)
            {
                heap.push(tamanho_bloco/2);
                heap.push(tamanho_bloco/2);
            }
            if(tamanho_bloco%2==0)
            {
                heap.push(tamanho_bloco/2);
                heap.push(tamanho_bloco/2 - 1);                  
            }
       }

        int resposta_final = heap.top();

        cout<<"Case #"<<t<<": ";

        if(resposta_final%2!=0) cout<<resposta_final/2<<" "<<resposta_final/2<<"\n";
        else
        { cout<<resposta_final/2<<" "<<resposta_final/2 - 1<<"\n";
        }
    }
}