#include <QVector>
#include <QTextStream>

QString solve(QString str, int K)
{
    int N = str.length();
    QVector<bool> arr(N);
    for (int i = 0; i < N; ++i)
    {
        arr[i] = (str[i] == '+');
    }

    int cntFlips = 0;

    for (int i = 0; i < N - K + 1; ++i)
    {
        if (arr[i])
        {
            continue;
        }

        ++cntFlips;

        for (int j = 0; j < K; ++j)
        {
            arr[i + j] = !arr[i + j];
        }
    }

    for (int i = N - K; i < N; ++i)
    {
        if (!arr[i])
        {
            return "IMPOSSIBLE";
        }
    }

    return QString::number(cntFlips);
}

int main(int, char**)
{
    QTextStream ins(stdin);
    QTextStream out(stdout);

    int T = QString(ins.readLine()).toInt();

    for (int i = 0; i < T; ++i)
    {
        int K;
        QString str;
        ins >> str >> K;
//        out << QString("Case #%1: ").arg(QString::number(i + 1)) << QString("%1").arg(solve(A, B, P),-8,'f',6) << endl;
        out << QString("Case #%1: ").arg(QString::number(i + 1)) << solve(str, K) << endl;
    }

    return 0;
}
