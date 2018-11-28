#include <QVector>
#include <QTextStream>

int getTidyCount(const QVector<int>& arr)
{
    for (int i = 1; i < arr.length(); ++i)
    {
        if (arr[i] < arr[i - 1])
        {
            return i;
        }
    }
    return arr.length();
}

int getDecrCount(const QVector<int>& arr, int cntTidy)
{
    for (int i = cntTidy - 1; i > 0; --i)
    {
        if (arr[i] > arr[i - 1])
        {
            return i;
        }
    }
    return arr[0] > 1 ? 0 : -1;
}

QString solve(QString str)
{
    int N = str.length();
    QVector<int> arr(N);
    for (int i = 0; i < N; ++i)
    {
        arr[i] = str[i].toLatin1() - '0';
    }

    int cntTidy = getTidyCount(arr);

    if (cntTidy == N)
    {
        return str;
    }

    int cntDecr = getDecrCount(arr, cntTidy);

    if (cntDecr < 0)
    {
        return QString(N - 1, '9');
    }

    QString ret = str.left(cntDecr);
    ret += ('0' + (arr[cntDecr] - 1));
    ret += QString(N - cntDecr - 1, '9');

    return ret;
}

int main(int, char**)
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();

    for (int i = 0; i < T; ++i)
    {
        QString str;
        ins >> str;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(str) << endl;
    }

    return 0;
}
