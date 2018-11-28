#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s;
    cin >> s;
    
    int len = (int)s.size();
    for (int i = 0, j = len - 1; i < j; ++i, --j)
    {
        char ch = s[i];
        s[i] = s[j];
        s[j] = ch;
    }
    
    //cout << s << endl;
    
    // kmp
    
    int fail[len];
    fail[0] = -1;
    for (int i = 1; i < len; ++i)
    {
        int cur = fail[i - 1];
        while (cur != -1 && s[cur + 1] != s[i]) cur = fail[cur];
        if (s[cur + 1] == s[i]) fail[i] = cur + 1; else fail[i] = -1;
    }
    
    //cout << "fail = "; for (int i = 0; i < len; ++i) cout << fail[i] << " "; cout << endl;
    
    // osuff
    int osuff[len];
    bool used[len];
    memset(osuff, -1, sizeof(osuff));
    memset(used, false, sizeof(used));
    for (int i = len - 1; i >= 0; --i)
    {
        int cur = i;
        while (!used[cur])
        {
            used[cur] = true;
            if (fail[cur] == -1) break;
            osuff[i - fail[cur]] = max(osuff[i - fail[cur]], fail[cur]);
            cur = fail[cur];
        }
    }
    osuff[0] = len - 1;
    
    cout << "osuff = "; for (int i = len - 1; i >= 0; --i) cout << osuff[i] + 1 << " "; cout << endl;
    
    return 0;
}
