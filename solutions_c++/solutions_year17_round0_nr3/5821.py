#include<iostream>
#include<string>
#include<forward_list>

using namespace std;
int main(){
    long long T, N, K,cont = 1, contK = 0;
    cin >> T;
    forward_list<long long> lista;
    while (T != 0){
        lista.clear();
        cin >> N;
        cin >> K;        
        while (contK != K){
            if(N % 2 == 0){
                lista.push_front(N / 2);
                lista.push_front((N / 2) - 1);
                if (contK == K - 1)
                    cout << "Case #" << cont << ": " << N / 2 << " " << (N / 2) - 1 << endl;  
                lista.sort(greater<long long>());
            }
            else{
                lista.push_front(N/2);
                lista.push_front(N/2);
                if (contK == K - 1)
                    cout << "Case #" << cont << ": " << N / 2 << " " << N / 2<< endl;
                lista.sort(greater<long long>());
            }
            if(K != 1){
                N = lista.front();
                lista.pop_front();
            }
            contK++;
        }
        int X = lista.front();
        lista.pop_front();
        int Y = lista.front();
        lista.pop_front();
        // cout << "Case #" << cont << ": " << X << " " << Y << endl; 
        T--;
        cont++;
        contK = 0;
    }
    return 0;
}