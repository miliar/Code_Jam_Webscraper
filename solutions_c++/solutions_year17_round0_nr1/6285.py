#include <QCoreApplication>
#include <QFile>
#include <QStringList>
#include <QTextStream>
#include <QDebug>
#include <QtGlobal>
#include <QDateTime>
#include <QList>
#include <QMap>
#include <QPair>

bool is_debug = false;

QString getAnswer(int K, QString Str) {
    if (is_debug) {
        qDebug() << "start getAnswer";
    }

    int res = 0;
    for(int i = 0, Ln = Str.length(); i < Ln; ++i) {
        if (Str.at(i) == '-') {
            if (i > Ln - K) {
                return "IMPOSSIBLE";
            }
            ++res;
            for (int j = 0; j < K; ++j) {
                Str[i + j] = Str.at(i + j) == '-' ? '+' : '-';
            }
        }
    }


    return QString::number(res);
}

int main(int argc, char *argv[])
{
    QCoreApplication a(argc, argv);

    QStringList params = QCoreApplication::arguments();
    if (params.count() < 3) {
        return 1;
    }

    qDebug() << params;
    qDebug() << params.at(1);
    QFile file_in(params.at(1));
    if (!file_in.open(QIODevice::ReadOnly | QIODevice::Text)) {
        return 2;
    }

    QTextStream in(&file_in);

    QFile file_out(params.at(2));
    if (!file_out.open(QIODevice::WriteOnly)) {
        return 3;
    }

    is_debug = true;//params.count() > 3 && params.at(3).compare("debug") == 0;

    QTextStream out(&file_out);
    QString line;
    int Idx = -1;
    int CaseNum = 0;
    QString answer;

    QDateTime start;
    QDateTime finish;
    QStringList sl;
    int line_type = 0;
    int K = 0;
    QString str;

    while (!in.atEnd()) {
        line = in.readLine();
        if (++Idx == 0) {
            if (is_debug) qDebug() << "Input case count " << line;
            continue;
        }

            sl = line.split(" ");
            str = sl.at(0);
            K = sl.at(1).toInt();
            if (is_debug) {
                qDebug() << "Current index " << Idx << K << str << line;
            }
            answer = "Case #" + QString::number(++CaseNum) + ": " + getAnswer(K, str);
            out << answer;
            endl(out);

        if (is_debug) {
            //qDebug() << "LineProcessed" << finish.toTime_t() - start.toTime_t();
        }

    }//*/
    return 0;
    //return a.exec();
}
