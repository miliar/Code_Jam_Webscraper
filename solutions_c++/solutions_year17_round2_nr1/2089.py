#include <bits/stdc++.h>

using namespace std;

int main(){

    int n, distance, horse, speed, inicio;
    double velocidade;

    cin >> n;

    for (int i = 1; i <= n; i++){
        cin >> distance >> horse;

        velocidade = 0;

        for (int j = 0; j < horse; j++){
            cin >> inicio >> speed;

            if ( ( (distance - inicio) / (double)speed) > velocidade)
                velocidade = (distance - inicio) / (double)speed;
        }

        cout << "Case #" << i << ": ";
        printf("%lf\n", distance / velocidade);
    }
}
