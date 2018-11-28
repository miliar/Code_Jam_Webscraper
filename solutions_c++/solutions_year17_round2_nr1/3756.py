#include <iostream>
#include <iomanip>

int main() {
    int T, D, N, K, S;
    double M, C;
    std::cin >> T;
    for ( int i = 0; i < T; i++ )
    {
        std::cin >> D >> N;
        M = -1.0;
        for ( int j = 0; j < N; j++ )
        {
            std::cin >> K >> S;
            C = (double)D / ( ( (double)D - (double)K ) / (double)S );
            if ( M < 0 || C < M )
            {
                M = C;
            }
        }
        std::cout << "Case #" << (i+1) << ": " << std::fixed << std::setprecision(6) << M << std::endl;
    }
    return 0;
}