#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t, test_case;
    cin >> test_case;
    for(int t = 1; t <= test_case; t++)
    {
        cout << "Case #" << t << ": ";
        string ss;
        cin >> ss;
        int arr[100];

        for(int i = 0; i < ss.length(); i++)
        {
            arr[i] = (char)ss[i] - (char)'0';
        }

        int s = 0, e = ss.length() - 1;
        while(s < e && arr[s] <= arr[s + 1])
        {
            s++;
        }
        if(s == e)
        {
            cout << ss << endl;
        }
        else
        {
            if(arr[s] == 1)
            {
                for(int i = 0; i < e; i++)
                    cout << '9';
                cout << endl;
            }
            else
            {
                int x = arr[s];
                int j = s;
                while(j >= 0 && arr[j] == x)
                {
                    j--;
                }
                arr[j+1]--;
                for(int i = 0; i <= j+1; i++)
                {
                    cout << arr[i];
                }
                for(int i = j + 1 + 1; i <= e; i++)
                {
                    arr[i] = 9;
                    cout << '9';
                }
                for(int i = 0; i < e; i++)
                {
                    if(arr[i] > arr[i+1])
                        cout << "FAILURE" << endl;
                }
                cout << endl;
            }
            
        }
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}