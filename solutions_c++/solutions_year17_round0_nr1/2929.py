#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int k;
void flip(bool arr[1009], int s)
{
    for(int i = s; i < s + k; i++)
        arr[i] = !arr[i];
}

void rflip(bool arr[1009], int e)
{
    for(int i = e; i > e - k; i--)
        arr[i] = !arr[i];
}

void print(bool arr[1009], int l)
{
    for(int i = 0; i < l; i++)
        cout << arr[i];
    cout << endl;
}

int main()
{
    freopen("input.txt", "r+", stdin);
    freopen("output.txt", "w", stdout);
    int t, test_case;
    cin >> test_case;
    for(int t = 1; t <= test_case; t++)
    {
        cout << "Case #" << t << ": ";
        string ss;
        cin >> ss;
        cin >> k;
        //cout << ss << " " << k;
        bool arr[1009] = {0};
        for(int i = 0; i < ss.length(); i++)
        {
            if(ss[i] == '+')
                arr[i] = 1;
            else
                arr[i] = 0;
        }

        int s = 0, e = ss.length() - 1;
        //cout << s << " " << e;
        int count = 0, ans = 0;
        while(s < e)
        {
            //print(arr, ss.length());
            if(arr[s] == 1)
            {
                while(s <= e && arr[s] == 1)
                    s++;
            }
            else
            {
                if(s + k - 1 > e)
                {
                    cout << "IMPOSSIBLE" << endl;
                    ans = 1;
                    break;
                }
                flip(arr, s);
                count++;
                if(arr[s] == 1)
                {
                    while(s <= e && arr[s] == 1)
                        s++;
                }
            }

            if(arr[e] == 1)
            {
                while(e >= s && arr[e] == 1)
                    e--;
            }
            else
            {
                if(e - k + 1 < s)
                {
                    cout << "IMPOSSIBLE" << endl;
                    ans = 1;
                    break;
                }
                rflip(arr, e);
                count++;
                if(arr[e] == 1)
                {
                    while(e >= s && arr[e] == 1)
                        e--;
                }
            }
        }
        if(ans == 0 && s == e && arr[s] == 0)
            cout << "IMPOSSIBLE" << endl;
        else if(ans == 0)
            cout << count << endl;
    }
    fclose(stdout);
    fclose(stdin);
    return 0;
}