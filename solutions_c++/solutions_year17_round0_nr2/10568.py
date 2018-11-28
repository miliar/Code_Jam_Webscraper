#include <iostream>

using namespace std;

void fillArray(int arr[], int arr_size)
{
    for(int i = 0; i < arr_size; ++i)
        arr[i] = 0;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    //int64_t x;
    //unsigned long long x;
    //Use any of the above for large data set

    int t, x, res = 0, temp = 0, arr[5];
    cin >> t;
    for(int i = 1; i <= t; ++i)
    {
        fillArray(arr, 5);
        res = 0;
        temp = 0;
        cin >> x;
        if(x < 10)
        {
            res = x;
        }
        else
        {
            for(int j = 10; j <= x; ++j)
            {
                int k = 0;
                int temp2 = j;
                temp = j;

                while(temp != 0)
                {
                    arr[k] = temp % 10;
                    temp = temp / 10;
                    ++k;
                }
                if((arr[0] >= arr[1]) && (arr[1] >= arr[2]) && (arr[2] >= arr[3]) && (arr[3] >= arr[4]))
                {
                    res = temp2;
                }
            }
        }
        cout << "Case #" << i << ": " << res << endl;
    }

    return 0;
}
