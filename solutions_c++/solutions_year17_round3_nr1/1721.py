#include <iostream>
#include <iomanip>

using namespace std;
long double pi = 3.14159265358979;

int main()
{


    int t;
    cin >> t;

    for(int test = 1;test<=t;test++)
    {
        long double answer = 0;
        int N,K;
        cin >> N >> K;
        long long int R[N];
        long long int H[N];
        bool used[N];
        for(int i = 0;i<N;i++)
        {
            cin >> R[i] >> H[i];
            used[i] = false;
        }

        //now find K -1 highest
        for(int i = 1;i<K;i++)
        {
            int best_i = 0;
            long double best_area = 0;
            for(int j = 0;j<N;j++)
            {
                if(2*pi*R[j]*H[j] > best_area and !used[j])
                {
                    best_i = j;
                    best_area = 2*pi*R[j]*H[j];
                }
            }
            answer += best_area;
            used[best_i] = true;

            //cout << R[best_i] << " " << H[best_i] << " " << best_area << " " << answer << endl;
        }

        //find best base
        int max_r_so_far = 0;
        for(int i = 0;i<N;i++)
        {
            if(used[i] and R[i] > max_r_so_far)
            {
                max_r_so_far = R[i];
            }
        }

        long double bestbase = 0;

        for(int i = 0;i<N;i++)
        {
            long double area_add_i = 0;
            if(!used[i])
            {
                if(R[i] < max_r_so_far)
                {
                    area_add_i = 2*pi*R[i]*H[i] + pi*max_r_so_far*max_r_so_far;
                }
                else
                {
                    area_add_i = 2*pi*R[i]*H[i] + pi*R[i]*R[i];
                }
            }
            if(area_add_i > bestbase)
            {
                bestbase = area_add_i;
            }
        }
        //cout << bestbase << endl;

        answer += bestbase;


        cout << "Case #" << test << ": " << setprecision(45) << answer + 0.0000000000001 << endl;
    }
}
