#include <iostream>
#include <string>

#define MAX_N 100
#define MAX_T 100
#define MAX_M 10000;
using namespace std;

int n;
int points;
bool avail_c[MAX_N+1];
bool avail_r[MAX_N+1];
bool avail_px[2 * MAX_N + 1];
bool avail_nx[2 * MAX_N + 1];
char final_map[MAX_N + 1][MAX_N + 1];
char original_map[MAX_N + 1][MAX_N + 1];
void disable_x(int r, int c)
{
    avail_nx[r - c + n + 1] = false;
    avail_px[r + c] = false;
}

void disable_rc(int r, int c)
{
    avail_r[r] = false;
    avail_c[c] = false;
}

void fill_rc(bool* a)
{
    for (int i = 1; i <= n; i++)
        a[i] = true;
}

void fill_x(bool* a)
{
    for (int i = 0; i <= 2 * MAX_N; i++)
        a[i] = false;
}

void fill_px()
{
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            avail_px[i + j] = true;
}

void fill_nx()
{
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            avail_nx[i - j + n + 1] = true;
}

void fill_map(char m[MAX_N + 1][MAX_N + 1])
{
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            m[i][j] = '.';
}

void init()
{
    int m;
    cin >> n >> m;
    fill_rc(avail_r);
    fill_rc(avail_c);
    fill_x(avail_px);
    fill_px();
    fill_x(avail_nx);
    fill_nx();
    fill_map(final_map);
    fill_map(original_map);
    int r, c;
    char ch;
    points = 0;
    while (m--)
    {
        cin >> ch >> r >> c;
        original_map[r][c] = ch;
        if (ch == 'x')
        {
            disable_rc(r, c);
            points++;
        }
        else if (ch == '+')
        {
            disable_x(r, c);
            points++;
        }
        else
        {
            disable_x(r, c);
            disable_rc(r, c);
            points += 2;
        }
    }
}

int get_avail_rc(bool* a)
{
    int result = 0;
    for (int i = 1; i <= n; i++)
        result += a[i];
    return result;
}

int get_avail_x(bool* a)
{
    int result = 0;
    for (int i = 2; i <= 2 * n; i++)
        result += a[i];
    return result;
}

void add_map(int r, int c, char ch)
{
    if (final_map[r][c] != '.' || original_map[r][c] != '.')
        ch = 'o';
    final_map[r][c] = ch;
    points++;
}

bool valid_x(int px, int nx)
{
    if ((px + nx - n - 1) % 2 != 0)
        return false;
    int r = (px + nx - n - 1) / 2;
    int c = (px - nx + n + 1) / 2;
    if (r < 1)
        return false;
    if (r > n)
        return false;
    if (c < 1)
        return false;
    if (c > n)
        return false;
    return true;
}
int partition(int arr[MAX_N * 2 + 1][2 * MAX_N + 2], const int left, const int right)
{
    const int mid = left + (right - left) / 2;
    const int pivot = arr[mid][0];
    // move the mid point value to the front.
    std::swap(arr[mid],arr[left]);
    int i = left + 1;
    int j = right;
    while (i <= j)
    {
        while(i <= j && arr[i][0] <= pivot)
        {
            i++;
        }

        while(i <= j && arr[j][0] > pivot)
        {
            j--;
        }

        if (i < j)
        {
            std::swap(arr[i], arr[j]);
        }
    }
    std::swap(arr[i - 1],arr[left]);
    return i - 1;
}

void quicksort(int arr[MAX_N * 2 + 1][2 * MAX_N + 2], const int left, const int right, const int sz)
{

    if (left >= right)
    {
        return;
    }


    int part = partition(arr, left, right);
    quicksort(arr, left, part - 1, sz);
    quicksort(arr, part + 1, right, sz);
}

void solve()
{
    int num_c = get_avail_rc(avail_c);
    int num_r = get_avail_rc(avail_r);
    int num_px = get_avail_x(avail_px);
    int num_nx = get_avail_x(avail_nx);
    if (num_r < num_c)
    {
        for (int i = 1; i <= n; i++)
            if (avail_r[i])
                for (int j = 1; j <= n; j++)
                    if (avail_c[j])
                    {
                        add_map(i, j, 'x');
                        avail_r[i] = false;
                        avail_c[j] = false;
                        break;
                    }
    }
    else
    {
        for (int j = 1; j <= n; j++)
            if (avail_c[j])
                for (int i = 1; i <= n; i++)
                    if (avail_r[i])
                    {
                        add_map(i, j, 'x');
                        avail_r[i] = false;
                        avail_c[j] = false;
                        break;
                    }
    }
    int candidate[MAX_N * 2 + 1][2 * MAX_N + 2] = {{0}};
    if (num_nx < num_px)
    {
        for (int i = 1; i<= n; i++)
            for (int j = 1; j <=n ; j++)
                if (avail_px[i + j] && avail_nx[i-j+n+1])
                {
                    candidate[i-j+n+1][0] = candidate[i-j+n+1][0] + 1;
                    candidate[i-j+n+1][1] = i-j+n+1;
                    int ra = candidate[i-j+n+1][0] + 1;
                    candidate[i-j+n+1][ra] = i+j;
                }
        quicksort(candidate, 0, 2*n, 2*n+1);
        for (int i = 0; i <= 2*n; i++)
            for (int j = 2; j <= candidate[i][0] + 1; j++)
            {
                int px = candidate[i][j];
                int nx = candidate[i][1];
                if (avail_px[px] && avail_nx[nx])
                {
                    int r = (px + nx - n - 1) / 2;
                    int c = (px - nx + n + 1) / 2;
                    add_map(r, c, '+');
                    avail_px[px] = false;
                    avail_nx[nx] = false;
                }
            }
    }
    else
    {
        for (int i = 1; i<= n; i++)
            for (int j = 1; j <=n ; j++)
                if (avail_px[i + j] && avail_nx[i-j+n+1])
                {
                    candidate[i + j][0] = candidate[i + j][0] + 1;
                    candidate[i + j][1] = i + j;
                    int ra = candidate[i + j][0] + 1;
                    candidate[i + j][ra] = i-j+n+1;
                }
        quicksort(candidate, 0, 2*n, 2*n+1);
        for (int i = 0; i <= 2*n; i++)
            for (int j = 2; j <= candidate[i][0] + 1; j++)
            {
                int px = candidate[i][1];
                int nx = candidate[i][j];
                if (avail_px[px] && avail_nx[nx])
                {
                    int r = (px + nx - n - 1) / 2;
                    int c = (px - nx + n + 1) / 2;
                    add_map(r, c, '+');
                    avail_px[px] = false;
                    avail_nx[nx] = false;
                }
            }
    }
    int num_points = 0;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (final_map[i][j] != '.')
                num_points++;
    cout << points << ' ' << num_points << endl;
    for (int i = 1; i <= n; i++)
        for (int j = 1; j <= n; j++)
            if (final_map[i][j] != '.')
                cout << final_map[i][j] << ' ' << i << ' ' << j << endl;
}

int main()
{
    int t;
    string s;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        init();
        cout << "Case #" << i << ": ";
        solve();
    }
    return 0;
}
